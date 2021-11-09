import { NgModule } from '@angular/core';

import { MatCardModule } from '@angular/material/card';
import { MatInputModule } from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule} from '@angular/common/http'

@NgModule({
  imports: [
      MatCardModule,
      MatInputModule,
      MatButtonModule,
      HttpClientModule,
      FormsModule,
      ReactiveFormsModule
  ],
  exports:[
      MatCardModule,
      MatInputModule,
      MatButtonModule,
      FormsModule,
      ReactiveFormsModule
  ]
})
export class LoginModule {}
