def conv_layer():
    return 1

def pooling_layer():
    return 1

def main():
    
    layer_type = ""
    while not (layer_type is "conv" or layer_type is "pool"):
        print("What type of layer is it? conv or pool")
        layer_type = input()

    if layer_type is "conv":
        kernels = -1
        print("How many kernels are there?")
        while kernels<=0:
            try:
                kernels= int(input())
            except:
                print("please enter an actual integer")

    print("What type of layer is it?")
    layer_type = input()

    print("What type of layer is it?")
    layer_type = input()

    #print(conv_layer())
    #print(pooling_layer())

main()