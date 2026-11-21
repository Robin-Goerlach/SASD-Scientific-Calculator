#include <sasd/scientific/rpn_engine.hpp>

#include <cmath>
#include <iomanip>
#include <iostream>
#include <locale>
#include <sstream>
#include <string>

namespace {
void print_stack(const sasd::scientific::RpnEngine& engine) {
    const auto& values = engine.values();
    if (values.empty()) { std::cout << "[empty]\n"; return; }
    for (std::size_t index = values.size(); index > 0; --index) {
        std::cout << index << ": " << std::setprecision(17) << values[index - 1] << '\n';
    }
}

bool parse_number(const std::string& text, double& value) {
    std::istringstream input(text);
    input.imbue(std::locale::classic());
    if (!(input >> value) || !std::isfinite(value)) return false;
    // Reject a trailing second token; blank trailing whitespace is harmless.
    std::string extra;
    return !(input >> extra);
}
} // namespace

int main() {
    sasd::scientific::RpnEngine engine;
    std::cout << "SASD Scientific Core / development CLI (not an iPhone app)\n"
                 "Commands: push N, +, -, *, /, dup, swap, drop, clear, stack, help, quit\n";
    std::string line;
    while (std::cout << "> " && std::getline(std::cin, line)) {
        sasd::scientific::Result result{};
        if (line == "quit" || line == "exit") break;
        if (line == "help") {
            std::cout << "push N -> append; binary operations use y (second) and x (top)\n";
            continue;
        }
        if (line == "stack") { print_stack(engine); continue; }
        if (line == "clear") { engine.clear(); print_stack(engine); continue; }
        if (line.starts_with("push ")) {
            double value = 0.0;
            if (!parse_number(line.substr(5), value)) {
                std::cerr << "error: expected finite decimal value\n";
                continue;
            }
            result = engine.push(value);
        } else if (line == "+") result = engine.add();
        else if (line == "-") result = engine.subtract();
        else if (line == "*") result = engine.multiply();
        else if (line == "/") result = engine.divide();
        else if (line == "dup") result = engine.duplicate();
        else if (line == "swap") result = engine.swap();
        else if (line == "drop") result = engine.drop();
        else { std::cerr << "error: unknown command\n"; continue; }
        if (!result.ok()) std::cerr << "error: " << sasd::scientific::error_message(result.error) << '\n';
        print_stack(engine);
    }
}
