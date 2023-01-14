from process_timer import spencer_timer

def main():
    timer = spencer_timer()
    timer.begin_timer("main")
    print("program begun")
    timer.end_timer("main")


if __name__ == "__main__":
    main()