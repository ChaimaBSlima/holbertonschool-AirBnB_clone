<p align="center">An AirBnB clone.</p>

# Description :house:

HolbertonBnB, a revolutionary web application, seamlessly blends database storage, a dynamic back-end API, and an intuitive front-end interface, creating a bespoke AirBnB clone.

The current project implementation is focused on the robust development of the back-end console.

# Classes :cl:
HolbertonBnB boasts an array of classes designed for diverse functionality:


||PUBLIC INSTANCE ATTRIBUTES|PUBLIC INSTANCE METHODS|PUBLIC CLASS ATTRIBUTES|PRIVATE CLASS ATTRIBUTES|
|--------------------------|------------------------|----------------------|----------------------|------------------------|
|**BaseModel**|`id`,`created_at`,`updated_at`|`save`,`to_dict`|||
|**FileStorage**||`all`,`new`,`save`,`reload`|`file_path`,`objects`||
|**User**|`email`,`password`,`first_name`,`last_name`||||
|**State**|`name`||||
|**City**|`state_id`,`name`||||
|**Amenity**|`name`||||
|**Place**|`city_id`,`user_id`,`name`,`description`,`number_rooms`,`number_bathrooms`,`max_guest`,`price_by_night`,`latitude`,`longitude`,`amenity_ids`||`place_id`,`user_id`,`text`||
|**Review**|`place_id`,`user_id`,`text`||||


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
