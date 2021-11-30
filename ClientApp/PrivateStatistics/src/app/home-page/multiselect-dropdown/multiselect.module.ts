import { CommonModule } from "@angular/common";
import { NgModule } from "@angular/core";
import { ReactiveFormsModule } from "@angular/forms";
import { MatButtonModule } from "@angular/material/button";
import { MatCardModule } from "@angular/material/card";
import { MatInputModule } from "@angular/material/input";
import { BrowserModule } from "@angular/platform-browser";
import { MultiselectDropdownComponent } from "./multiselect-dropdown.component";

@NgModule({
  imports: [
    BrowserModule,
    CommonModule,
    MatCardModule,
    MatInputModule,
    MatButtonModule,
    ReactiveFormsModule,
  ],
  exports: [MultiselectDropdownComponent],
  declarations: [MultiselectDropdownComponent],
})
export class MultiSelectModule {}