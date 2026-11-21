#pragma once

#include <cstddef>
#include <string_view>
#include <vector>

namespace sasd::scientific {

// MVP engine: generic modern RPN arithmetic, not a historical calculator emulator.
// Stack order is bottom ... top, with the top at values().back().
enum class Error { none, stack_underflow, division_by_zero, invalid_operand, numeric_overflow };

struct Result {
    Error error{Error::none};
    [[nodiscard]] constexpr bool ok() const noexcept { return error == Error::none; }
};

[[nodiscard]] std::string_view error_message(Error error) noexcept;

class RpnEngine {
public:
    // Reject non-finite input rather than importing NaN/Inf into persistent state.
    [[nodiscard]] Result push(double value);
    [[nodiscard]] Result duplicate();
    [[nodiscard]] Result swap();
    [[nodiscard]] Result drop();
    void clear() noexcept;
    [[nodiscard]] Result add();
    [[nodiscard]] Result subtract(); // y - x
    [[nodiscard]] Result multiply();
    [[nodiscard]] Result divide();   // y / x
    [[nodiscard]] std::size_t depth() const noexcept { return values_.size(); }
    [[nodiscard]] const std::vector<double>& values() const noexcept { return values_; }

private:
    enum class BinaryOp { add, subtract, multiply, divide };
    [[nodiscard]] Result binary(BinaryOp op);
    std::vector<double> values_{};
};

} // namespace sasd::scientific
