from process_timer import spencer_timer
from camera_process import  camera_operator

def main():
    timer = spencer_timer()
    timer.begin_timer("main")


    print("program begun")

    camera = camera_operator()
    camera.startscreen()

    timer.end_timer("main")


if __name__ == "__main__":
    main()