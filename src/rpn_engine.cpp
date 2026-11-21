#include <sasd/scientific/rpn_engine.hpp>

#include <cmath>

namespace sasd::scientific {

std::string_view error_message(Error error) noexcept {
    switch (error) {
        case Error::none: return "ok";
        case Error::stack_underflow: return "stack underflow";
        case Error::division_by_zero: return "division by zero";
        case Error::invalid_operand: return "invalid operand";
        case Error::numeric_overflow: return "non-finite result";
    }
    return "unknown error";
}

Result RpnEngine::push(double value) {
    if (!std::isfinite(value)) return {Error::invalid_operand};
    values_.push_back(value);
    return {};
}

Result RpnEngine::duplicate() {
    if (values_.empty()) return {Error::stack_underflow};
    values_.push_back(values_.back());
    return {};
}

Result RpnEngine::swap() {
    if (values_.size() < 2) return {Error::stack_underflow};
    const double last = values_.back();
    values_.back() = values_[values_.size() - 2];
    values_[values_.size() - 2] = last;
    return {};
}

Result RpnEngine::drop() {
    if (values_.empty()) return {Error::stack_underflow};
    values_.pop_back();
    return {};
}

void RpnEngine::clear() noexcept { values_.clear(); }

Result RpnEngine::binary(BinaryOp op) {
    if (values_.size() < 2) return {Error::stack_underflow};
    const double x = values_.back();
    const double y = values_[values_.size() - 2];
    if (op == BinaryOp::divide && x == 0.0) return {Error::division_by_zero};

    double result = 0.0;
    switch (op) {
        case BinaryOp::add: result = y + x; break;
        case BinaryOp::subtract: result = y - x; break;
        case BinaryOp::multiply: result = y * x; break;
        case BinaryOp::divide: result = y / x; break;
    }
    if (!std::isfinite(result)) return {Error::numeric_overflow};
    // Commit only on success: errors leave stack depth and contents untouched.
    values_[values_.size() - 2] = result;
    values_.pop_back();
    return {};
}

Result RpnEngine::add() { return binary(BinaryOp::add); }
Result RpnEngine::subtract() { return binary(BinaryOp::subtract); }
Result RpnEngine::multiply() { return binary(BinaryOp::multiply); }
Result RpnEngine::divide() { return binary(BinaryOp::divide); }

} // namespace sasd::scientific
