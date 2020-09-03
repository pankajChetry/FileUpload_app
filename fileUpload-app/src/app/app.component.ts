import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title :string;
  upload_file:File;

  onTitleChanged(event:any) {
    this.title = event.target.value;
  }

  onFileChanged(event:any) {
    this.upload_file = event.target.files[0];
  }

}
