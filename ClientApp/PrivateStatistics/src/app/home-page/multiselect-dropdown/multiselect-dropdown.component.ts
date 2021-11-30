import { Component, OnInit } from '@angular/core';
import { FormControl } from '@angular/forms';

@Component({
  selector: 'app-multiselect-dropdown',
  templateUrl: './multiselect-dropdown.component.html',
  styleUrls: ['./multiselect-dropdown.component.scss'],
})
export class MultiselectDropdownComponent implements OnInit {
  hospitalsList = ['Arcadia', 'Spiridon', 'Tineretului', 'Saint Marie'];

  hospitalsFormControl = new FormControl();

  constructor() {}

  ngOnInit(): void {}
}
