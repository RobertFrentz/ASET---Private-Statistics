from pythonrv import rv

import users.views as views


@rv.monitor(stat=views.Statistics.post, login=views.Login.post)
@rv.spec(when=rv.POST)
def simple_specification(event):
    if event.called_function == event.fn.stat:
        assert event.fn.login.called
