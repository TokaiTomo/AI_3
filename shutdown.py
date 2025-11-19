option = input("Shut down?(Yes/No): ")
def shutdown(ans):

    if ans == "Yes":
        print("Shutting down")
        print("Shut Down")
    if ans == "No":
        print("Aborting shut down")
        print("Shut down aborted")
shutdown(option)