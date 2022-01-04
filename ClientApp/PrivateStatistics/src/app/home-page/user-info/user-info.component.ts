import { Component, Input, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-user-info',
  templateUrl: './user-info.component.html',
  styleUrls: ['./user-info.component.scss'],
})
export class UserInfoComponent implements OnInit {
  @Input() username: String | null;

  constructor(private router: Router) {}

  ngOnInit(): void {}

  logout(): void{
    this.router.navigate(['/login']);
  }
}
