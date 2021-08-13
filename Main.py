def conv_layer(in_h, in_w, in_d, kernels, kernel_size, padding, stride):
    new_h = int((in_h-kernel_size+(2*padding))/stride)+1
    new_w = int((in_w-kernel_size+(2*padding))/stride)+1
    new_d = kernels
    return new_h, new_w, new_d

def pooling_layer(in_h, in_w, in_d, window_size, stride):
    new_h = int((in_h-window_size)/stride)+1
    new_w = int((in_w-window_size)/stride)+1
    new_d = in_d
    return new_h, new_w, new_d

def main():
    in_w = -1
    print("Enter input width:")
    while in_w<=0:
        try:
            in_w= int(input())
        except:
            print("please enter an actual integer")

    in_h = -1
    print("Enter input height:")
    while in_h<=0:
        try:
            in_h= int(input())
        except:
            print("please enter an actual integer")

    in_d = -1
    print("Enter input depth:")
    while in_d<=0:
        try:
            in_d= int(input())
        except:
            print("please enter an actual integer")

    layer_type = ""
    while not (layer_type == "conv" or layer_type == "pool"):
        print("What type of layer is it? conv or pool")
        layer_type = input()
        print(layer_type)
    
    if layer_type == "conv":
        kernels = -1
        print("How many kernels are there?")
        while kernels<=0:
            try:
                kernels= int(input())
            except:
                print("please enter an actual integer")
        
        kernel_size = -1
        print("Enter kernel size:")
        while kernel_size<=0:
            try:
                kernel_size= int(input())
            except:
                print("please enter an actual integer")

        padding = -1
        print("Enter padding size:")
        while padding<0:
            try:
                padding= int(input())
            except:
                print("please enter an actual integer")
        stride = -1
        print("Enter stride size:")
        while stride<=0:
            try:
                stride= int(input())
            except:
                print("please enter an actual integer")
        out_h, out_w, out_d = conv_layer(in_h, in_w, in_d, kernels, kernel_size, padding, stride)

    elif layer_type == "pool":
        window_size = -1
        print("Enter window size:")
        while window_size<=0:
            try:
                window_size= int(input())
            except:
                print("please enter an actual integer")
        stride = -1
        print("Enter stride:")
        while stride<=0:
            try:
                stride= int(input())
            except:
                print("please enter an actual integer")
        out_h, out_w, out_d = pooling_layer(in_h, in_w, in_d, window_size, stride)
    print(out_h, out_w, out_d)

main()