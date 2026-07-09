def hanoi_solver(n: int) -> str:
    rods: list[list[int]] = [list(range(n, 0, -1)), [], []]
    
    states: list[str] = []
    
    def record_state():
        states.append(f"{rods[0]} {rods[1]} {rods[2]}")

    def move(n_disks: int, source: int, target: int, auxiliary: int) -> None:
        if n_disks > 0:
            move(n_disks - 1, source, auxiliary, target)
            
            disk = rods[source].pop()
            rods[target].append(disk)
            record_state()
            
            move(n_disks - 1, auxiliary, target, source)

    record_state()
    
    move(n, 0, 2, 1)
    
    return "\n".join(states)


if __name__ == "__main__":
    print("--- 2 Disks ---")
    print(hanoi_solver(2))
    
    print("\n--- 3 Disks ---")
    print(hanoi_solver(3))