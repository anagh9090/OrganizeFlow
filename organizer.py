import os
import shutil

# --- Configuration: The Ultimate File Type Mapping ---
FILE_TYPE_MAP = {
    # 📝 Documents & Text
    ('txt', 'doc', 'docx', 'pdf', 'rtf', 'odt', 'pages', 'epub', 'md', 'log', 'tex', 'wps', 'wks', 'wri', 'info', 'msg', 'eml', 'err', 'nfo'): 'Documents',
    
    # 🖼️ Images & Graphics (Rasters, Vectors, RAW, Scientific)
    ('jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'tif', 'svg', 'ico', 'jfif', 'webp', 'heic', 'raw', 'cr2', 'nef', 'dng', 'arw', 'orf', 'sr2', 'ai', 'psd', 'cdr', 'eps', 'indd', 'pub', 'tga', 'pcx', 'wmf', 'emf', 'exr'): 'Images',
    
    # 🎥 Videos & Movies
    ('mp4', 'mkv', 'flv', 'avi', 'mov', 'wmv', 'webm', '3gp', 'm4v', 'mpeg', 'vob', 'ogv', 'ts', 'mts', 'm2ts', 'rm', 'swf', 'dat', 'rts', 'srt', 'sub', 'ass', 'idx'): 'Videos',
    
    # 🎧 Audio & Music
    ('mp3', 'wav', 'aac', 'flac', 'ogg', 'wma', 'm4a', 'aiff', 'mid', 'midi', 'opus', 'cda', 'ape', 'dts', 'mod', 'it', 's3m', 'xm'): 'Audio',
    
    # 📦 Archives & Compressed Files
    ('zip', 'rar', '7z', 'tar', 'gz', 'bz2', 'xz', 'iso', 'img', 'cab', 'rpm', 'deb', 'msu', 'z', 'lha', 'ace', 'sit', 'sitx'): 'Archives',
    
    # 💻 Source Code & Development (General Languages)
    ('py', 'js', 'java', 'c', 'cpp', 'h', 'hpp', 'cs', 'go', 'rb', 'swift', 'kt', 'php', 'pl', 'lua', 'r', 'dart', 'scala', 'clj', 'groovy', 'vb', 'f', 'pas', 'asm', 'cob', 'sh', 'bat', 'cmd', 'ps1'): 'Source_Code',

    # 🌐 Web Files & Frontend
    ('html', 'htm', 'css', 'scss', 'less', 'xml', 'json', 'yaml', 'yml', 'jsx', 'tsx', 'vue', 'astro', 'gsp', 'jsp', 'asp', 'aspx', 'rss', 'atom'): 'Web_Files',

    # 📊 Spreadsheets & Data
    ('xls', 'xlsx', 'xlsm', 'xlsb', 'ods', 'csv', 'tsv', 'dat', 'numbers', 'dif', 'sylk', 'prn'): 'Spreadsheets',
    
    # 🖼️ Presentations
    ('ppt', 'pptx', 'key', 'odp', 'pps', 'ppsx', 'pot', 'thmx'): 'Presentations',

    # ⚙️ Executables & Installers
    ('exe', 'msi', 'dmg', 'appimage', 'apk', 'jar', 'run', 'bin', 'vbs', 'wsf', 'com', 'scf', 'gadget'): 'Executables',

    # 🗃️ Databases & Data Dumps
    ('sql', 'db', 'sqlite', 'mdb', 'accdb', 'bak', 'frm', 'myd', 'myi', 'dbf', 'gdb', 'fdb', 'mdf', 'ndf'): 'Databases',

    # ✒️ Fonts
    ('ttf', 'otf', 'woff', 'woff2', 'eot', 'fon', 'fnt'): 'Fonts',
    
    # 🖥️ System & Configuration
    ('ini', 'cfg', 'conf', 'sys', 'reg', 'dll', 'drv', 'tmp', 'lock', 'dmp', 'plist', 'htaccess', 'service', 'desktop'): 'System_Configuration',
    
    # 🧊 3D Models & CAD
    ('3ds', 'obj', 'fbx', 'dae', 'stl', 'blend', 'ma', 'mb', 'max', 'skp', 'lwo', 'iges', 'step', 'stp', 'jt', 'vrml'): '3D_Models_CAD',

    # 🗺️ Geographic Information Systems (GIS)
    ('shp', 'shx', 'dbf', 'prj', 'kml', 'kmz', 'gpx', 'geojson', 'las', 'laz'): 'GIS_Files',
    
    # 🔬 Scientific & Engineering Data
    ('mat', 'nb', 'cdf', 'fit', 'fits', 'hdf', 'he5', 'nc', 'grd', 'fem', 'stp'): 'Scientific_Data',

    # 💾 Disc & Virtualization
    ('iso', 'img', 'toast', 'cue', 'ccd', 'nrg', 'vdi', 'vmdk', 'vhd', 'vhdx', 'ova', 'ovf', 'qcow2', 'box', 'vagrant', 'dockerfile'): 'Virtual_Disc',
}

# Folder name for files that don't match any specified extension
OTHER_FOLDER = 'Others'
# --- End Configuration ---


def organize_files(directory_path):
    """
    Organizes files in the specified directory into subfolders based on file extension.
    """
    print(f"Starting organization in: {directory_path}")
    
    # Get all items in the directory
    for item_name in os.listdir(directory_path):
        source_path = os.path.join(directory_path, item_name)
        
        # Skip directories and the script itself
        if os.path.isdir(source_path) or item_name == os.path.basename(__file__):
            continue
            
        # Get the file extension and clean it
        _, extension = os.path.splitext(item_name)
        extension = extension[1:].lower() 

        # Determine the target folder name
        target_folder = None
        for extensions, folder_name in FILE_TYPE_MAP.items():
            if extension in extensions:
                target_folder = folder_name
                break
        
        if target_folder is None:
            target_folder = OTHER_FOLDER

        target_dir_path = os.path.join(directory_path, target_folder)
        
        # Create the target folder if it doesn't exist
        if not os.path.exists(target_dir_path):
            os.makedirs(target_dir_path)

        destination_path = os.path.join(target_dir_path, item_name)
        
        # Move the file with collision handling
        try:
            if os.path.exists(destination_path):
                # Simple collision avoidance: append a number (e.g., file(1).ext)
                base, ext = os.path.splitext(item_name)
                counter = 1
                unique_name_found = False
                while not unique_name_found:
                    new_item_name = f"{base}({counter}){ext}"
                    temp_destination_path = os.path.join(target_dir_path, new_item_name)
                    if not os.path.exists(temp_destination_path):
                        destination_path = temp_destination_path
                        unique_name_found = True
                    counter += 1
                print(f"Collision detected, renamed to: {new_item_name}")

            shutil.move(source_path, destination_path)
            print(f"Moved: {item_name} -> {target_folder}")
        except Exception as e:
            print(f"Error moving {item_name}: {e}")

if __name__ == "__main__":
    # Get the directory where the script is being run from (the current working directory)
    current_directory = os.getcwd()
    organize_files(current_directory)
    print("\nFile organization complete!")
