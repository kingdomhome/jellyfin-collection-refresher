import os
import xml.etree.ElementTree as ET

def unlock_collection_files(root_dir):
    """
    Recursively searches for collection.xml files and changes the
    <LockData> element to 'false' in each file.

    Args:
        root_dir (str): The root directory to start the search from.
    """
    for foldername, subfolders, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.lower() == "collection.xml":
                filepath = os.path.join(foldername, filename)
                try:
                    tree = ET.parse(filepath)
                    root = tree.getroot()
                    lock_data_element = root.find('LockData')
                    if lock_data_element is not None:
                        lock_data_element.text = 'false'
                        tree.write(filepath, encoding='utf-8', xml_declaration=True)
                        print(f"Updated '{filepath}': <LockData> set to false")
                    else:
                        print(f"Warning: <LockData> element not found in '{filepath}'")
                except ET.ParseError:
                    print(f"Error parsing XML in '{filepath}'. Skipping file.")
                except OSError as e:
                    print(f"Error accessing or writing to '{filepath}': {e}")

if __name__ == "__main__":
    target_directory = input("Enter the root directory to search for collection.xml files: ")
    unlock_collection_files(target_directory)
    print("Script finished.")