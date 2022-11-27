# Instagram-Image-Grid-Maker-and-Photo-Uploader
Python program to divide an image of choice to a grid specified by user and upload each image to instagram

Follow the below mentioned steps to use.

!!! The script is by default set for 6 row 3 column image division set !!!

1. Store image file in the 'Images' folder as (name of image should not contain underscores. Ideal name examples are img1, random-image, image-11, etc)
2. Go to 'upload.py' python script and in the 'filename' variable type in image file's name & in the 'extension' variable type in image extension (ex. jpg, jpeg, webp etc)
3. After putting name of your file in variable put number of rows (i.e Number of vertical images you want).
4. After putting row count value, put number of column count (i.e Number of horizontal images, Max value for instagram is 3).
5. Type in your username of instagram handle in 'user' variable and password in 'passw' variable.
6. Run 'upload.py' on IDE or run 'upload.py' in command prompt/terminal by navigating to the stored folder and executing the command "python3 upload.py"

Following the step 1-6 will run the file and you will shortly see the images being uploaded to the instagram handle specified.

In order to do the task again and again with different images, you must first delete the 'config' folder which is created in the same directory 
as of other files of task.
