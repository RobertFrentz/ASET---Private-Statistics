import { ComponentFixture, TestBed } from '@angular/core/testing';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { RouterTestingModule } from '@angular/router/testing';
import { of } from 'rxjs';

import { LoginPageComponent } from './login-page.component';
import { LoginPageFacade } from './login-page-facade.service';

describe('LoginPageComponent', () => {
  let facade: LoginPageFacade;
  let component: LoginPageComponent;
  let fixture: ComponentFixture<LoginPageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [
        RouterTestingModule
      ],
      declarations: [ LoginPageComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    facade = TestBed.inject(LoginPageFacade);
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
