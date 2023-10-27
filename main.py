import time
class NQueens:
    def __init__(self):
        self.size = 8
        positions = []
        # Початковий стан дошки, всі ферзі розташовані у перший стовпчик.
        positions = [4, 0, 6, 4, 3, 7, 5, 5]
        print("Початкове розташування: ", positions)
        try:
            start_time = time.time()
            max_execution_time = 60  # Обмеження на час виконання програми (60 секунд).
            self.put_queen(positions, 0, start_time, max_execution_time)
        except:
            print((time.time() - start_time), "seconds")

    def put_queen(self, positions, target_row, start_time, max_execution_time):
        current_time = time.time()
        # Перевіряємо, чи не перевищено обмеження на час виконання програми.
        if current_time - start_time >= max_execution_time:
            print("Час виконання перевищив обмеження.")
            raise

        for column in range(self.size):
            if target_row == self.size:
                # Якщо вдалося розмістити ферзя в кожному рядку, виводимо розв'язок та завершуємо виконання.
                print("Результат розташування: ", positions)
                raise
            elif self.check_place(positions, target_row, (column + positions[target_row]) % self.size):
                # Розміщуємо ферзя в поточному стовпці та переходимо до наступного рядка.
                positions[target_row] = (column + positions[target_row]) % self.size
                self.put_queen(positions, target_row + 1, start_time, max_execution_time)

    def check_place(self, positions, ocuppied_rows, column):
        for i in range(ocuppied_rows):
            if positions[i] == column or \
                    positions[i] - i == column - ocuppied_rows or \
                    positions[i] + i == column + ocuppied_rows:
                return False
        return True


# Створюємо об'єкт класу NQueens, щоб розпочати пошук розв'язку.
NQueens()
