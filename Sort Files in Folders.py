import os
import shutil

path = "<Your Folder name here Format: C:/Users/User_name/Downloads/>"
names =os.listdir(path)

folder_name = ['Misc Files','Developer Files','Disk Image Files','Compressed Files','Settings Files','System Files','Plugin Files','Web Files','Game Files','Database','Spreadsheet','3d','Images','Text Files','Executables','Videos','Music','pdf','Presentation','Data Files']
for x in range(0,19):
    if not os.path.exists(path+folder_name[x]):
        os.makedirs(path+folder_name[x])

for files in names:
    if ".png" in files :
        shutil.move(path+files, path+'Images/'+files)
    if ".jpg" in files :
        shutil.move(path+files, path+'Images/'+files)
    if ".tif" in files :
        shutil.move(path+files, path+'Images/'+files)
    if ".tiff" in files :
        shutil.move(path+files, path+'Images/'+files)
    if ".bmp" in files :
        shutil.move(path+files, path+'Images/'+files)
    if ".jpeg" in files :
        shutil.move(path+files, path+'Images/'+files)
    if ".gif" in files :
        shutil.move(path+files, path+'Images/'+files)
    if ".eps" in files :
        shutil.move(path+files, path+'Images/'+files)
    if ".raw" in files :
        shutil.move(path+files, path+'Images/'+files)
    if ".cr2" in files :
        shutil.move(path+files, path+'Images/'+files)
    if ".nef" in files :
        shutil.move(path+files, path+'Images/'+files)
    if ".orf" in files :
        shutil.move(path+files, path+'Images/'+files)
    if ".sr2" in files :
        shutil.move(path+files, path+'Images/'+files)
    if ".txt" in files:
        shutil.move(path+files, path+'Text Files/'+files)
    if ".fpt" in files :
        shutil.move(path+files, path+'Text Files/'+files)
    if ".docx" in files :
        shutil.move(path+files, path+'Text Files/'+files)
    if ".rtf" in files :
        shutil.move(path+files, path+'Text Files/'+files)
    if ".log" in files :
        shutil.move(path+files, path+'Text Files/'+files)
    if ".doc" in files :
        shutil.move(path+files, path+'Text Files/'+files)
    if ".ppt" in files :
        shutil.move(path+files, path+'Presentation/'+files)
    if ".pptx" in files :
        shutil.move(path+files, path+'Presentation/'+files)
    if ".csv" in files :
        shutil.move(path+files, path+'Data Files/'+files)
    if ".key" in files :
        shutil.move(path+files, path+'Data Files/'+files)
    if ".keychain" in files :
        shutil.move(path+files, path+'Data Files/'+files)
    if ".dat" in files :
        shutil.move(path+files, path+'Data Files/'+files)
    if ".sdf" in files :
        shutil.move(path+files, path+'Data Files/'+files)
    if ".tar" in files :
        shutil.move(path+files, path+'Data Files/'+files)
    if ".xml" in files :
        shutil.move(path+files, path+'Data Files/'+files)
    if ".vcf" in files :
        shutil.move(path+files, path+'Data Files/'+files)
    if ".aif" in files :
        shutil.move(path+files, path+'Music/'+files)
    if ".iff" in files :
        shutil.move(path+files, path+'Music/'+files)
    if ".m3u" in files :
        shutil.move(path+files, path+'Music/'+files)
    if ".m4a" in files :
        shutil.move(path+files, path+'Music/'+files)
    if ".mid" in files :
        shutil.move(path+files, path+'Music/'+files)
    if ".mp3" in files :
        shutil.move(path+files, path+'Music/'+files)
    if ".mpa" in files :
        shutil.move(path+files, path+'Music/'+files)
    if ".wav" in files :
        shutil.move(path+files, path+'Music/'+files)
    if ".wma" in files :
        shutil.move(path+files, path+'Music/'+files)
    if ".3g2" in files :
        shutil.move(path+files, path+'Videos/'+files)
    if ".3gp" in files :
        shutil.move(path+files, path+'Videos/'+files)
    if ".asf" in files :
        shutil.move(path+files, path+'Videos/'+files)
    if ".avi" in files :
        shutil.move(path+files, path+'Videos/'+files)
    if ".flv" in files :
        shutil.move(path+files, path+'Videos/'+files)
    if ".m4v" in files :
        shutil.move(path+files, path+'Videos/'+files)
    if ".mov" in files :
        shutil.move(path+files, path+'Videos/'+files)
    if ".mp4" in files :
        shutil.move(path+files, path+'Videos/'+files)
    if ".mpg" in files :
        shutil.move(path+files, path+'Videos/'+files)
    if ".rm" in files :
        shutil.move(path+files, path+'Videos/'+files)
    if ".srt" in files :
        shutil.move(path+files, path+'Videos/'+files)
    if ".swf" in files :
        shutil.move(path+files, path+'Videos/'+files)
    if ".mkv" in files :
        shutil.move(path+files, path+'Videos/'+files)
    if ".vob" in files :
        shutil.move(path+files, path+'Videos/'+files)
    if ".wmv" in files :
        shutil.move(path+files, path+'Videos/'+files)
    if ".3dm" in files :
        shutil.move(path+files, path+'3d/'+files)
    if ".3ds" in files :
        shutil.move(path+files, path+'3d/'+files)
    if ".max" in files :
        shutil.move(path+files, path+'3d/'+files)
    if ".obj" in files :
        shutil.move(path+files, path+'3d/'+files)
    if ".xlr" in files :
        shutil.move(path+files, path+'Spreadsheet/'+files)
    if ".xls" in files :
        shutil.move(path+files, path+'Spreadsheet/'+files)
    if ".xlsx" in files :
        shutil.move(path+files, path+'Spreadsheet/'+files)
    if ".db" in files :
        shutil.move(path+files, path+'Database/'+files)
    if ".sql" in files :
        shutil.move(path+files, path+'Database/'+files)
    if ".accdb" in files :
        shutil.move(path+files, path+'Database/'+files)
    if ".dbf" in files :
        shutil.move(path+files, path+'Database/'+files)
    if ".mdb" in files :
        shutil.move(path+files, path+'Database/'+files)
    if ".pdb" in files :
        shutil.move(path+files, path+'Database/'+files)
    if ".apk" in files :
        shutil.move(path+files, path+'Executables/'+files)
    if ".app" in files :
        shutil.move(path+files, path+'Executables/'+files)
    if ".bat" in files :
        shutil.move(path+files, path+'Executables/'+files)
    if ".cgi" in files :
        shutil.move(path+files, path+'Executables/'+files)
    if ".com" in files :
        shutil.move(path+files, path+'Executables/'+files)
    if ".exe" in files :
        shutil.move(path+files, path+'Executables/'+files)
    if ".gadget" in files :
        shutil.move(path+files, path+'Executables/'+files)
    if ".jar" in files :
        shutil.move(path+files, path+'Executables/'+files)
    if ".wsf" in files :
        shutil.move(path+files, path+'Executables/'+files)
    if ".b" in files :
        shutil.move(path+files, path+'Game Files/'+files)
    if ".dem" in files :
        shutil.move(path+files, path+'Game Files/'+files)
    if ".gam" in files :
        shutil.move(path+files, path+'Game Files/'+files)
    if ".nes" in files :
        shutil.move(path+files, path+'Game Files/'+files)
    if ".rom" in files :
        shutil.move(path+files, path+'Game Files/'+files)
    if ".sav" in files :
        shutil.move(path+files, path+'Game Files/'+files)
    if ".pdf" in files :
        shutil.move(path+files, path+'pdf/'+files)
    if ".asp" in files :
        shutil.move(path+files, path+'Web Files/'+files)
    if ".aspx" in files :
        shutil.move(path+files, path+'Web Files/'+files)
    if ".css" in files :
        shutil.move(path+files, path+'Web Files/'+files)
    if ".htm" in files :
        shutil.move(path+files, path+'Web Files/'+files)
    if ".html" in files :
        shutil.move(path+files, path+'Web Files/'+files)
    if ".js" in files :
        shutil.move(path+files, path+'Web Files/'+files)
    if ".jsp" in files :
        shutil.move(path+files, path+'Web Files/'+files)
    if ".php" in files :
        shutil.move(path+files, path+'Web Files/'+files)
    if ".rss" in files :
        shutil.move(path+files, path+'Web Files/'+files)
    if ".crx" in files :
        shutil.move(path+files, path+'Plugin Files/'+files)
    if ".plugin" in files :
        shutil.move(path+files, path+'Plugin Files/'+files)
    if ".fnt" in files :
        shutil.move(path+files, path+'Plugin Files/'+files)
    if ".fon" in files :
        shutil.move(path+files, path+'Plugin Files/'+files)
    if ".otf" in files :
        shutil.move(path+files, path+'Plugin Files/'+files)
    if ".ttf" in files :
        shutil.move(path+files, path+'Plugin Files/'+files)
    if ".cab" in files :
        shutil.move(path+files, path+'System Files/'+files)
    if ".deskthemepack" in files :
        shutil.move(path+files, path+'System Files/'+files)
    if ".dll" in files :
        shutil.move(path+files, path+'System Files/'+files)
    if ".ico" in files :
        shutil.move(path+files, path+'System Files/'+files)
    if ".sys" in files :
        shutil.move(path+files, path+'System Files/'+files)
    if ".lnk" in files :
        shutil.move(path+files, path+'System Files/'+files)
    if ".dmp" in files :
        shutil.move(path+files, path+'System Files/'+files)
    if ".drv" in files :
        shutil.move(path+files, path+'System Files/'+files)
    if ".ini" in files :
        shutil.move(path+files, path+'Settings Files/'+files)
    if ".cfg" in files :
        shutil.move(path+files, path+'Settings Files/'+files)
    if ".prf" in files :
        shutil.move(path+files, path+'Settings Files/'+files)
    if ".7z" in files :
        shutil.move(path+files, path+'Compressed Files/'+files)
    if ".cbr" in files :
        shutil.move(path+files, path+'Compressed Files/'+files)
    if ".deb" in files :
        shutil.move(path+files, path+'Compressed Files/'+files)
    if ".gz" in files :
        shutil.move(path+files, path+'Compressed Files/'+files)
    if ".pkg" in files :
        shutil.move(path+files, path+'Compressed Files/'+files)
    if ".rar" in files :
        shutil.move(path+files, path+'Compressed Files/'+files)
    if ".rpm" in files :
        shutil.move(path+files, path+'Compressed Files/'+files)
    if ".tar.gz" in files :
        shutil.move(path+files, path+'Compressed Files/'+files)
    if ".zip" in files :
        shutil.move(path+files, path+'Compressed Files/'+files)
    if ".zipx" in files :
        shutil.move(path+files, path+'Compressed Files/'+files)
    if ".bin" in files :
        shutil.move(path+files, path+'Disk Image Files/'+files)
    if ".dmg" in files :
        shutil.move(path+files, path+'Disk Image Files/'+files)
    if ".iso" in files :
        shutil.move(path+files, path+'Disk Image Files/'+files)
    if ".mdf" in files :
        shutil.move(path+files, path+'Disk Image Files/'+files)
    if ".vcd" in files :
        shutil.move(path+files, path+'Disk Image Files/'+files)
    if ".c" in files :
        shutil.move(path+files, path+'Developer Files/'+files)
    if ".class" in files :
        shutil.move(path+files, path+'Developer Files/'+files)
    if ".cpp" in files :
        shutil.move(path+files, path+'Developer Files/'+files)
    if ".cs" in files :
        shutil.move(path+files, path+'Developer Files/'+files)
    if ".java" in files :
        shutil.move(path+files, path+'Developer Files/'+files)
    if ".pl" in files :
        shutil.move(path+files, path+'Developer Files/'+files)
    if ".py" in files :
        shutil.move(path+files, path+'Developer Files/'+files)
    if ".sh" in files :
        shutil.move(path+files, path+'Developer Files/'+files)
    if ".vb" in files :
        shutil.move(path+files, path+'Developer Files/'+files)
    if ".vcxproj" in files :
        shutil.move(path+files, path+'Developer Files/'+files)
    if ".jsp" in files :
        shutil.move(path+files, path+'Developer Files/'+files)
    if ".servlet" in files :
        shutil.move(path+files, path+'Developer Files/'+files)
    if ".ics" in files :
        shutil.move(path+files, path+'Misc Files/'+files)
    if ".msi" in files :
        shutil.move(path+files, path+'Misc Files/'+files)
    if ".part" in files :
        shutil.move(path+files, path+'Misc Files/'+files)
    if ".torrent" in files :
        shutil.move(path+files, path+'Misc Files/'+files)
    