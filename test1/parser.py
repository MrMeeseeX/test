import xml.etree.ElementTree as ET
import shutil

root_node = ET.parse('config.xml').getroot()
print(root_node)

source_value, dest_value, file_name = '', '', ''

for tag in root_node.findall('file'):
    source_value = tag.get('source_path')
    if source_value is not None: print(source_value)
    dest_value = tag.get('destination_path')
    if dest_value is not None: print(dest_value)
    file_name = tag.get('file_name')
    if file_name is not None: print(file_name)

file_to_copy = source_value + '\\' + file_name

shutil.copy(file_to_copy, dest_value)