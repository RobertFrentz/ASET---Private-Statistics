import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';

@Component({
  selector: 'app-select-dropdown',
  templateUrl: './select-dropdown.component.html',
  styleUrls: ['./select-dropdown.component.scss'],
})
export class SelectDropdownComponent implements OnInit {
  @Input() dropdownLabel: string = "default";
  @Input() fieldsList: string[] = [];
  @Output() selectedDrowpdownValue: EventEmitter<string> = new EventEmitter();
  constructor() {}

  ngOnInit(): void {}

  onSelectValue(matValue: any): void{
    this.selectedDrowpdownValue.emit(matValue.value);
  }
}
