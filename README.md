<h1 align="center">AirBnB clone - The console</h1>

# Description :house:

HolbertonBnB, a revolutionary web application, seamlessly blends database storage, a dynamic back-end API, and an intuitive front-end interface, creating a bespoke AirBnB clone.

The current project implementation is focused on the robust development of the back-end console.

# Classes :cl:
HolbertonBnB boasts an array of classes designed for diverse functionality:


||PUBLIC INSTANCE ATTRIBUTES|PUBLIC INSTANCE METHODS|PUBLIC CLASS ATTRIBUTES|PRIVATE CLASS ATTRIBUTES|
|--------------------------|------------------------|----------------------|----------------------|------------------------|
|**BaseModel**|`id`<br>`created_at`<br>`updated_at`|`save`<br>`to_dict`|||
|**FileStorage**||`all`<br>`new`<br>`save`<br>`reload`|| `file_path`<br>`objects`|
|**User**|Inherits from `BaseModel`|""|`email`<br>`password`<br>`first_name`<br>`last_name`||
|**State**|Inherits from `BaseModel`|""| `name`||
|**City**|Inherits from `BaseModel`|""|`state_id`<br>`name`||
|**Amenity**|Inherits from `BaseModel`|""|`name`||
|**Place**|Inherits from `BaseModel`|""|`city_id`<br>`user_id`<br>`name`<br>`description`<br>`number_rooms`<br>`number_bathrooms`<br>`max_guest`<br>`price_by_night`<br>`latitude`<br>`longitude`<br>`amenity_ids`||
|**Review**|Inherits from `BaseModel`|""|`place_id`<br>`user_id`<br>`text`||


# Console :computer:

The HolbertonBnB console serves as a command-line interpreter designed to manage the backend of HolbertonBnB. It enables the manipulation of all classes used by the application, facilitated by calls on the `storage` object.

## Usage of the Console

The console can be run in both interactive and non-interactive modes. To run it in non-interactive mode, pipe commands into an execution of the `console.py` file.

```
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
$
```

# Storage :
The abstracted storage engine is defined in the [FileStorage](./models/engine/file_storage.py) class. The `FileStorage` class handles the management of all classes mentioned above. Upon initialization, HolbertonBnB creates an instance of `FileStorage` named `storage`, which is loaded or reloaded from the `file.json` JSON file. As class instances are created, updated, or deleted, the `storage` object tracks and updates the corresponding changes in the `file.json`.

# Commands:

### Create
To create an object use format "create <ClassName>" 
```
	(hbnb) create BaseModel
```
### Show
To show an instance based on the class name and id. 
```
	(hbnb) show BaseModel 4848-4444-8888.
```
### Destroy
To Delete an instance of an object use "destroy <ClassName> id". 
```
	(hbnb) destroy BaseModel 4848-4444-8888.
```
### All
all or all <class name> 
```
	(hbnb) all or all State
```
### Update
Updates an instance based on the class name and id:
```
	(hbnb) update BaseModel 4848-4444-8888 email "7689@holbertonstudents.com"
```

### Quit
quit or EOF

### Help
help or help <command> 

```
	(hbnb) help or help quit
	 Defines quit option
	(hbnb) 
```

# Authors

- [@ChaimaBSlima](https://github.com/ChaimaBSlima)


# 🚀 About Me
I'm a Machine Learning developer...
