import GPUtil

def get_gpu_names():
    try:
        # Get the list of GPU devices
        gpus = GPUtil.getGPUs()

        if not gpus:
            print("No GPU devices found.")
            return

        # Print GPU names
        print("GPU Names:")
        for gpu in gpus:
            print(f"- {gpu.name}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_gpu_names()