# dcf.py
# FIN 439 Lab 06
# KISS: standard library only, one file, one command.

# -------------------------
# TRAINING INPUTS
# -------------------------
TRAINING_FCFF = 100.0
TRAINING_GROWTH = [0.08, 0.06, 0.05, 0.04, 0.03]
TRAINING_WACC = 0.10
TRAINING_TERMINAL_GROWTH = 0.03
TRAINING_CASH = 50.0
TRAINING_DEBT = 300.0
TRAINING_SHARES = 50.0
TRAINING_TARGET_PRICE = 30.00

TRAINING_WACC_GRID = [0.09, 0.10, 0.11]
TRAINING_G_GRID = [0.02, 0.03, 0.04]
GROWTH_SHIFT_LOW = -0.05
GROWTH_SHIFT_HIGH = 0.10

# -------------------------
# ORACLE INPUTS
# USD millions except price/share
# -------------------------
ORCL_HISTORICAL_FCFF = -19666.474  # FY2026: CFO + after-tax interest - capex

# Negative FCFF exception: use an explicit five-year FCFF forecast.
# FY2027-FY2031 estimate, NOT company guidance.
ORCL_FCFF_PATH = [-20000.0, 0.0, 25000.0, 55000.0, 65000.0]

ORCL_WACC = 0.114
ORCL_TERMINAL_GROWTH = 0.03
ORCL_CASH = 31289.0
ORCL_DEBT = 129541.0
ORCL_SHARES = 2914.0
ORCL_TARGET_PRICE = 156.61

ORCL_WACC_GRID = [0.104, 0.114, 0.124]
ORCL_G_GRID = [0.02, 0.03, 0.04]

# Reverse DCF bounds for Oracle's explicit FCFF path, in USD millions.
FCFF_SHIFT_LOW = -10000.0
FCFF_SHIFT_HIGH = 10000.0


def dcf_from_growth(starting_fcff, growth_rates, wacc, terminal_growth,
                    cash, debt, shares):
    if terminal_growth >= wacc:
        return None

    fcff = []
    current = starting_fcff

    for growth in growth_rates:
        current = current * (1 + growth)
        fcff.append(current)

    pv_explicit = sum(
        cash_flow / ((1 + wacc) ** year)
        for year, cash_flow in enumerate(fcff, start=1)
    )

    terminal_value = fcff[-1] * (1 + terminal_growth) / (wacc - terminal_growth)
    pv_terminal = terminal_value / ((1 + wacc) ** 5)
    enterprise_value = pv_explicit + pv_terminal
    equity_value = enterprise_value + cash - debt
    value_per_share = equity_value / shares
    terminal_share = pv_terminal / enterprise_value

    return {
        "fcff": fcff,
        "pv_explicit": pv_explicit,
        "terminal_value": terminal_value,
        "pv_terminal": pv_terminal,
        "enterprise_value": enterprise_value,
        "equity_value": equity_value,
        "value_per_share": value_per_share,
        "terminal_share": terminal_share,
    }


def dcf_from_path(fcff_path, wacc, terminal_growth, cash, debt, shares):
    if terminal_growth >= wacc:
        return None

    pv_explicit = sum(
        cash_flow / ((1 + wacc) ** year)
        for year, cash_flow in enumerate(fcff_path, start=1)
    )

    terminal_value = fcff_path[-1] * (1 + terminal_growth) / (wacc - terminal_growth)
    pv_terminal = terminal_value / ((1 + wacc) ** 5)
    enterprise_value = pv_explicit + pv_terminal
    equity_value = enterprise_value + cash - debt
    value_per_share = equity_value / shares
    terminal_share = pv_terminal / enterprise_value

    return {
        "fcff": fcff_path,
        "pv_explicit": pv_explicit,
        "terminal_value": terminal_value,
        "pv_terminal": pv_terminal,
        "enterprise_value": enterprise_value,
        "equity_value": equity_value,
        "value_per_share": value_per_share,
        "terminal_share": terminal_share,
    }


def print_twelve_lines(result):
    for year, cash_flow in enumerate(result["fcff"], start=1):
        print(f"FCFF Year {year}: {cash_flow:.4f}")
    print(f"PV of explicit FCFF: {result['pv_explicit']:.4f}")
    print(f"Terminal value, Year 5: {result['terminal_value']:.4f}")
    print(f"PV of terminal value: {result['pv_terminal']:.4f}")
    print(f"Enterprise value: {result['enterprise_value']:.4f}")
    print(f"Equity value: {result['equity_value']:.4f}")
    print(f"Value per share: {result['value_per_share']:.4f}")
    print(f"PV of TV / enterprise value: {result['terminal_share']:.4f}")


def print_growth_grid(starting_fcff, growth_rates, wacc_values, g_values,
                      cash, debt, shares):
    print("WACC \\ g      " + "  ".join(f"{g:>8.1%}" for g in g_values))

    for wacc in wacc_values:
        cells = []
        for g in g_values:
            if g >= wacc:
                cells.append(" INVALID")
            else:
                result = dcf_from_growth(
                    starting_fcff, growth_rates, wacc, g, cash, debt, shares
                )
                cells.append(f"{result['value_per_share']:8.2f}")
        print(f"{wacc:>8.1%}      " + "  ".join(cells))


def print_path_grid(fcff_path, wacc_values, g_values, cash, debt, shares):
    print("WACC \\ g      " + "  ".join(f"{g:>8.1%}" for g in g_values))

    for wacc in wacc_values:
        cells = []
        for g in g_values:
            if g >= wacc:
                cells.append(" INVALID")
            else:
                result = dcf_from_path(fcff_path, wacc, g, cash, debt, shares)
                cells.append(f"{result['value_per_share']:8.2f}")
        print(f"{wacc:>8.1%}      " + "  ".join(cells))


def reverse_growth_shift():
    # Refuse a bracket if either endpoint would push any growth rate to -100% or below.
    if any(g + GROWTH_SHIFT_LOW <= -1.0 for g in TRAINING_GROWTH):
        print("No solution: lower bound creates growth <= -100%.")
        return
    if any(g + GROWTH_SHIFT_HIGH <= -1.0 for g in TRAINING_GROWTH):
        print("No solution: upper bound creates growth <= -100%.")
        return

    def value(shift):
        shifted_growth = [g + shift for g in TRAINING_GROWTH]
        return dcf_from_growth(
            TRAINING_FCFF,
            shifted_growth,
            TRAINING_WACC,
            TRAINING_TERMINAL_GROWTH,
            TRAINING_CASH,
            TRAINING_DEBT,
            TRAINING_SHARES,
        )["value_per_share"]

    low = GROWTH_SHIFT_LOW
    high = GROWTH_SHIFT_HIGH
    low_value = value(low)
    high_value = value(high)

    if not min(low_value, high_value) <= TRAINING_TARGET_PRICE <= max(low_value, high_value):
        print("No solution in the growth-shift bracket.")
        return

    for _ in range(100):
        middle = (low + high) / 2
        if value(middle) < TRAINING_TARGET_PRICE:
            low = middle
        else:
            high = middle

    shift = (low + high) / 2

    print(f"Target price: ${TRAINING_TARGET_PRICE:.2f}")
    print(f"Solved uniform growth shift: {shift:+.4%} "
          f"({shift * 100:+.2f} percentage points)")
    print("Held fixed: starting FCFF, WACC, terminal growth, cash, debt, diluted shares.")


def reverse_oracle_fcff_shift():
    # Oracle has negative starting FCFF, so shifting growth rates would grow a loss.
    # Solve instead for one uniform USD-million shift to the explicit five-year FCFF path.
    def value(shift):
        shifted_path = [fcff + shift for fcff in ORCL_FCFF_PATH]
        return dcf_from_path(
            shifted_path,
            ORCL_WACC,
            ORCL_TERMINAL_GROWTH,
            ORCL_CASH,
            ORCL_DEBT,
            ORCL_SHARES,
        )["value_per_share"]

    low = FCFF_SHIFT_LOW
    high = FCFF_SHIFT_HIGH
    low_value = value(low)
    high_value = value(high)

    if not min(low_value, high_value) <= ORCL_TARGET_PRICE <= max(low_value, high_value):
        print("No solution in the FCFF-shift bracket.")
        return

    for _ in range(100):
        middle = (low + high) / 2
        if value(middle) < ORCL_TARGET_PRICE:
            low = middle
        else:
            high = middle

    shift = (low + high) / 2
    implied_path = [fcff + shift for fcff in ORCL_FCFF_PATH]

    print(f"Target price: ${ORCL_TARGET_PRICE:.2f}")
    print(f"Solved uniform FCFF shift: {shift:+,.2f} USD millions per year")
    print("Price-implied FCFF path: " +
          ", ".join(f"{fcff / 1000:.2f}B" for fcff in implied_path))
    print("Held fixed: WACC, terminal growth, cash, debt, diluted shares.")
    print("Note: FCFF shift is used because Oracle's starting FCFF is negative.")


print("===== TRAINING CASE: 12 REQUIRED LINES =====")
training = dcf_from_growth(
    TRAINING_FCFF,
    TRAINING_GROWTH,
    TRAINING_WACC,
    TRAINING_TERMINAL_GROWTH,
    TRAINING_CASH,
    TRAINING_DEBT,
    TRAINING_SHARES,
)
print_twelve_lines(training)

print("\n===== TRAINING SENSITIVITY GRID ($/share) =====")
print_growth_grid(
    TRAINING_FCFF,
    TRAINING_GROWTH,
    TRAINING_WACC_GRID,
    TRAINING_G_GRID,
    TRAINING_CASH,
    TRAINING_DEBT,
    TRAINING_SHARES,
)

print("\n===== TRAINING REVERSE DCF =====")
reverse_growth_shift()

print("\n===== ORACLE: 12 REQUIRED LINES =====")
print(f"Historical FY2026 FCFF used to identify negative-FCFF exception: "
      f"{ORCL_HISTORICAL_FCFF:.4f}")
oracle = dcf_from_path(
    ORCL_FCFF_PATH,
    ORCL_WACC,
    ORCL_TERMINAL_GROWTH,
    ORCL_CASH,
    ORCL_DEBT,
    ORCL_SHARES,
)
print_twelve_lines(oracle)

print("\n===== ORACLE SENSITIVITY GRID ($/share) =====")
print_path_grid(
    ORCL_FCFF_PATH,
    ORCL_WACC_GRID,
    ORCL_G_GRID,
    ORCL_CASH,
    ORCL_DEBT,
    ORCL_SHARES,
)

print("\n===== ORACLE REVERSE DCF =====")
reverse_oracle_fcff_shift()
