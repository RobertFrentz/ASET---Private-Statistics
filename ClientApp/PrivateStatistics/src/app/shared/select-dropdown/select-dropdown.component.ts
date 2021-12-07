import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-select-dropdown',
  templateUrl: './select-dropdown.component.html',
  styleUrls: ['./select-dropdown.component.scss'],
})
export class SelectDropdownComponent implements OnInit {
  @Input() dropdownLabel: string = "default";
  @Input() fieldsList: string[] = [];

  constructor() {}

  ngOnInit(): void {}
}
