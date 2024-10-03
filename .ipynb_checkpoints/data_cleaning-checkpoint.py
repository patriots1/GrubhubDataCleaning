import json

inputfl = open('grubhub_neu_scrubbing.json')
input_ds = dict(json.load(inputfl))

output_ds = {}
# create output dictionary
output_ds['Restaurants'] = []
# iterate through input dictionary
for key in input_ds:
    # create a local dictionary to hold values for this restaurant
    restaurant_dc = {}
    # extract and store the latitude and longitude
    lat = input_ds[key]['restaurant']['latitude']
    lon = input_ds[key]['restaurant']['longitude']
    # extract and store the name in the name key
    restaurant_dc['Name'] = key
    # create an empty list for the dishes key, loop below will fill it.
    restaurant_dc['Dishes'] = []
    # this dataset has 2 lists to iterate through, so 2 for loops.
    for index in range(0, len(input_ds[key]['restaurant']['menu_category_list'])):
        for index2 in range(0, len(input_ds[key]['restaurant']['menu_category_list'][index]['menu_item_list'])):
            # extract key and value pairs for easier iterating.
            menu_item_ls = list(input_ds[key]['restaurant']['menu_category_list'][index]['menu_item_list'][index2].values())
            # name in index 4, item description in index 5.
            item_name = menu_item_ls[4]
            item_desc = menu_item_ls[5]
            # item image url in index 27, some are empty, so check for nulls.
            item_image_url = ''
            if bool(menu_item_ls[27]): 
                item_image_url = menu_item_ls[27]['base_url'] + menu_item_ls[27]['public_id']
            # create a dictionary to store dish data.
            dishes_dc = {'name': item_name, 'description': item_desc, 'imageLink': item_image_url}
            # append the dish dictionary to a list of dishes.
            restaurant_dc['Dishes'].append(dishes_dc)
    # add location to the dictionary
    restaurant_dc['Location'] = [lat, lon]
    # append restaurant to the output dictionary (values are in a list)
    output_ds['Restaurants'].append(restaurant_dc)

    with open('clean_neu_restaurants.json', 'w') as outputfl:
        json.dump(output_ds, outputfl, indent = 4)