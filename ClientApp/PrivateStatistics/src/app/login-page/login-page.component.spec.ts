import { ComponentFixture, TestBed, tick } from '@angular/core/testing';
import { of } from 'rxjs';

import { LoginPageComponent } from './login-page.component';

describe('LoginPageComponent', () => {
  let component: LoginPageComponent;
  let fixture: ComponentFixture<LoginPageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ LoginPageComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(LoginPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it(`should have as title 'Login'`, () => {
    expect(component.title).toEqual('Login');
  });

  it('should call getLoginResponse when logging user', async () => {
    const spy = spyOn<any>(component, 'getLoginResponse').and.returnValue(of(true));
    component.loginForm.get('username')?.setValue('Test1Username');
    component.loginForm.get('password')?.setValue('Test1Password');
    component.submit();
    fixture.detectChanges();

    expect(spy).toHaveBeenCalled();
  });
});
