#include <sasd/scientific/rpn_engine.hpp>

#include <cstdlib>
#include <iostream>
#include <limits>
#include <vector>

namespace {
void expect(bool condition, const char* message) {
    if (!condition) { std::cerr << "FAILED: " << message << '\n'; std::exit(EXIT_FAILURE); }
}
void push(sasd::scientific::RpnEngine& engine, double value) {
    expect(engine.push(value).ok(), "push must succeed");
}
void expect_stack(const sasd::scientific::RpnEngine& engine, const std::vector<double>& values) {
    expect(engine.values() == values, "stack contents/order must match");
}
} // namespace

int main() {
    using sasd::scientific::Error;
    sasd::scientific::RpnEngine s;
    expect(s.add().error == Error::stack_underflow, "empty arithmetic fails");
    expect(s.duplicate().error == Error::stack_underflow, "empty dup fails");
    expect(s.drop().error == Error::stack_underflow, "empty drop fails");
    push(s, 10.0); push(s, 4.0);
    expect(s.subtract().ok(), "subtract succeeds"); expect_stack(s, {6.0});
    push(s, 2.0); expect(s.divide().ok(), "divide succeeds"); expect_stack(s, {3.0});
    push(s, 4.0); expect(s.multiply().ok(), "multiply succeeds"); expect_stack(s, {12.0});
    push(s, 8.0); expect(s.add().ok(), "add succeeds"); expect_stack(s, {20.0});
    expect(s.duplicate().ok(), "dup succeeds"); expect_stack(s, {20.0, 20.0});
    push(s, 5.0); expect(s.swap().ok(), "swap succeeds"); expect_stack(s, {20.0, 5.0, 20.0});
    expect(s.drop().ok(), "drop succeeds"); expect_stack(s, {20.0, 5.0});
    push(s, 0.0); const auto old = s.values();
    expect(s.divide().error == Error::division_by_zero, "divide zero reports error");
    expect_stack(s, old); // Failed operations must not damage the state.
    expect(s.push(std::numeric_limits<double>::quiet_NaN()).error == Error::invalid_operand,
           "NaN rejected");
    expect_stack(s, old);
    s.clear(); expect(s.depth() == 0, "clear empties stack");
    push(s, std::numeric_limits<double>::max()); push(s, 2.0);
    const auto before_overflow = s.values();
    expect(s.multiply().error == Error::numeric_overflow, "overflow reports error");
    expect_stack(s, before_overflow);
    std::cout << "All initial core tests passed\n";
}
