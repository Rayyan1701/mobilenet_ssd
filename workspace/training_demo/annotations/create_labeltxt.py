def label_map_v1(id,name):
    with open(r'C:\Users\Dell\OneDrive\Desktop\Tensorflow\workspace\training_demo\annotations', 'a') as the_file:
        the_file.write('item\n')
        the_file.write('{\n')
        the_file.write('id :{}'.format(id))
        the_file.write('\n')
        the_file.write("name : {}".format(name))
        the_file.write('\n')
        the_file.write('}\n')
    
label_map_v1(1,'aluminium') 
label_map_v1(2,'can')
label_map_v1(3,'glass')
label_map_v1(4,'kitchen')
label_map_v1(5,'plastic')
label_map_v1(6,'cloth')
label_map_v1(7,'wood')
    