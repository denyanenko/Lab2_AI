import time
import random

# region LDFS Algorithm Implementation
class NQueens:
    def __init__(self, start):
        self.size = 8
        positions=start[:]
        self.state_count = 0  # Лічильник для кількості станів
        try:
            start_time = time.time()
            max_execution_time = 60  # Обмеження на час виконання програми (60 секунд).
            self.put_queen(positions, 0, start_time, max_execution_time)
        except:
            print((time.time() - start_time), "seconds")
            print("Кількість станів:", self.state_count)  # Вивід кількості станів

    def put_queen(self, positions, target_row, start_time, max_execution_time):
        current_time = time.time()
        # Перевіряємо, чи не перевищено обмеження на час виконання програми.
        if current_time - start_time >= max_execution_time:
            print("Час виконання перевищив обмеження.")
            raise

        for column in range(self.size):
            self.state_count += 1  # Збільшення лічильника підрахунку станів
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
# endregion

# region A* Algorithm Implementation
class Node():
    def __init__(self, parent=None, state=None):
        self.parent = parent
        self.state = state
        self.collisions = [0, 0, 0, 0, 0, 0, 0, 0]
        self.h = 0

    def __eq__(self, other):
        return self.state == other.state


def astar(start):
    start_node = Node(None, start)
    start_node.h = heuristic(start, start_node.collisions)

    open_list = []
    closed_list = []

    open_list.append(start_node)

    start_time = time.time()
    max_execution_time = 60  # Обмеження на час виконання програми (60 секунд).
    state_count = 0  # Лічильник для кількості станів

    while len(open_list) > 0:
        current_node = open_list[0]
        current_index = 0
        # Перевірка часу виконання
        if (time.time() - start_time) > max_execution_time:
            print("Час виконання перевищив обмеження.")
            return None
        for index, item in enumerate(open_list):
            if item.h < current_node.h:
                current_node = item
                current_index = index
            elif item.h > current_node.h + 2:
                open_list.remove(item)

        open_list.pop(current_index)
        closed_list.append(current_node)

        if current_node.h == 0:
            print("Результат розташування: ", current_node.state)
            print((time.time() - start_time), "seconds")
            print("Кількість станів: ", state_count)
            return None

        children = []
        for collisioned in range(0, 8):
            if current_node.collisions[collisioned]:
                for new_state in [1, 2, 3, 4, 5, 6, 7]:
                    new_node = Node(current_node, current_node.state.copy())

                    new_node.state[collisioned] = (new_node.state[collisioned] + new_state) % 8

                    children.append(new_node)
        for child in children:
            state_count += 1
            skip = False
            for closed_child in closed_list:
                if child == closed_child:
                    skip = True
            if skip: continue

            child.h = heuristic(child.state, child.collisions)

            for open_node in open_list:
                if child == open_node and child.h >= open_node.h:
                    skip = True
            if skip: continue

            open_list.append(child)


def heuristic(state, collisions):
    h = 0
    rowLock = -1
    upperDiagLock = -1
    lowerDiagLock = -1
    for i in range(0, 8):
        for j in range(i + 1, 8):
            if state[i] == state[j] and rowLock != i:
                rowLock = i
                collisions[i] = collisions[j] = 1
                h += 1
            elif state[i] - state[j] == i - j and upperDiagLock != i:
                upperDiagLock = i
                collisions[i] = collisions[j] = 1
                h += 1
            elif state[i] - state[j] == - (i - j) and lowerDiagLock != i:
                lowerDiagLock = i
                collisions[i] = collisions[j] = 1
                h += 1
    return h
# endregion

def main():
    start = []
    for i in range(0, 8):
        start.append(random.randint(0, 7))
    print("Початкове розташування: ", start,"\n")
    print("LDFS")
    NQueens(start)
    print()
    print("A*")
    astar(start)


if __name__ == '__main__':
    main()

