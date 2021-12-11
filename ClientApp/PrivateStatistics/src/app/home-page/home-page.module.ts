import { CommonModule } from "@angular/common";
import { NgModule } from "@angular/core";
import { ReactiveFormsModule } from "@angular/forms";
import { MatButtonModule } from "@angular/material/button";
import { MatCardModule } from "@angular/material/card";
import { MatInputModule } from "@angular/material/input";
import { MatTableModule } from '@angular/material/table';
import { BrowserModule } from "@angular/platform-browser";
import { LoginModule } from "../login-page/login.module";
import { HomePageComponent } from "./home-page.component";
import { MultiselectDropdownComponent } from "./multiselect-dropdown/multiselect-dropdown.component";
import { MatSelectModule } from '@angular/material/select';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { UserInfoComponent } from './user-info/user-info.component';
import { StatisticsComponent } from './statistics/statistics.component';
import { DisplayStatisticsComponent } from './statistics/display-statistics/display-statistics.component';
import { DisplayChartsComponent } from './statistics/display-charts/display-charts.component';
import { NgxEchartsModule } from "ngx-echarts";
import { SharedModule } from "../shared/shared.module";
import { DisplayStatisticLineComponent } from './statistics/display-statistics/display-statistic-line/display-statistic-line.component';
import { StatisticsHistoryComponent } from './statistics/statistics-history/statistics-history.component';

@NgModule({
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    CommonModule,
    MatCardModule,
    MatInputModule,
    MatButtonModule,
    MatSelectModule,
    MatTableModule,
    ReactiveFormsModule,
    LoginModule,
    SharedModule,
    NgxEchartsModule.forRoot({
      echarts: () => import('echarts'),
    }),
  ],
  exports: [],
  declarations: [
    HomePageComponent,
    MultiselectDropdownComponent,
    UserInfoComponent,
    StatisticsComponent,
    DisplayStatisticsComponent,
    DisplayChartsComponent,
    DisplayStatisticLineComponent,
    StatisticsHistoryComponent,
  ],
})
export class HomePageModule {}