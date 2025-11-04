from loguru import logger
import csv, datetime, os

# ---------- Base Functions ---------- #
def fun1(x, y):
    """Add two numbers."""
    logger.info(f"Adding {x} + {y}")
    result = x + y
    log_result("add", x, y, result)
    return result

def fun2(x, y):
    """Subtract y from x."""
    logger.info(f"Subtracting {x} - {y}")
    result = x - y
    log_result("sub", x, y, result)
    return result

def fun3(x, y):
    """Multiply two numbers."""
    logger.info(f"Multiplying {x} * {y}")
    result = x * y
    log_result("mul", x, y, result)
    return result

def fun4(x, y, z):
    """Sum three numbers."""
    logger.info(f"Summing {x}, {y}, {z}")
    result = x + y + z
    log_result("sum3", x, y, result)
    return result

# ---------- NEW: Smart Calculator ---------- #
def smart_calculator(x, y):
    """
    Adaptive calculator that decides operation automatically:
      - both positive → add
      - both negative → multiply
      - mixed signs   → subtract
    """
    if x >= 0 and y >= 0:
        op, result = "smart_add", fun1(x, y)
    elif x < 0 and y < 0:
        op, result = "smart_mul", fun3(x, y)
    else:
        op, result = "smart_sub", fun2(x, y)
    log_result(op, x, y, result)
    return result

# ---------- Helper: Log results ---------- #
def log_result(operation, x, y, result):
    os.makedirs("data", exist_ok=True)
    with open("data/results.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.datetime.now(), operation, x, y, result])
