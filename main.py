from src.valueObjects.Operation import Operation

sum_operation = Operation('+', '1', '2', '3', '3').resolve()
minus_operation = Operation('-', '1', '2', '3', '3').resolve()
product_operation = Operation('*', '1', '2', '3', '3').resolve()
division_operation = Operation('/', '1', '2', '3', '3').resolve()

print(f"Resultado suma: {sum_operation}")
print(f"Resultado resta: {minus_operation}")
print(f"Resultado multiplicacion: {product_operation}")
print(f"Resultado division: {division_operation}")