import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title :string;
  uploadedfile:File;

  constructor(private http: HttpClient){}

  onTitleChanged(event:any) {
    this.title = event.target.value;
  }

  onFileChanged(event:any) {
    this.uploadedfile = event.target.files[0];
  }
   
  upload(){
    const uploadData = new FormData();
    uploadData.append('title', this.title);
    uploadData.append('uploadedfile', this.uploadedfile, this.uploadedfile.name);
    this.http.post('http://localhost:8000/fileupload/', uploadData).subscribe(
      data => console.log(data),
      error => console.log(error)
    ); 
  }

}
