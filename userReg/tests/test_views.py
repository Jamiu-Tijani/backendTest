from userReg.models import userData
from userReg.tests.test_setup import TestSetUp
from django.core.files.uploadedfile import SimpleUploadedFile
import json
import ast
import os


class TestViews(TestSetUp):
    def test_user_is_created_wfu(self):
        """
        To test user is created without file upload
        this also affirms that user model is working
        """
        res = self.client.post(self.userReg_url,self.user_data, format ="json")
    
        self.assertEqual(res.status_code, 201) 

    
    def test_img_file_upload(self):
        """
        to test image file is uploaded
        """
        with open(self.imageUrl, 'rb') as infile: #open image file to be uploaded
            avatar = SimpleUploadedFile('icon.jpg', infile.read())
            print(avatar)
        json_data = ast.literal_eval(json.dumps(self.user_data)) #serialize the json data
        json_data["avatar"] = avatar
        self.client.post(self.userReg_url,data=json_data,  format="multipart")
        uploadedUrl = userData.objects.get(username=self.user_data["username"]).imageURL()
        os.remove(uploadedUrl) # delete uploaded file
        org_URL = str(self.imageUrl)
        org_filename = org_URL.split('/')[-3:][2]#origin file name
        uploaded_filename = uploadedUrl.split('/')[-3:][2]#uploaded filename
        self.assertEqual(uploaded_filename,org_filename)  
