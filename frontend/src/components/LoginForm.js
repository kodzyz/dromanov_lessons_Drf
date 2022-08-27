//0:27
import React from 'react'

class LoginForm extends React.Component {

    constructor(props) {
        super(props)

        this.state = {
            'login': '',
            'password': ''
        }
    }

    render () {
        return (
            <div>
                <form>
                    <input type="text" name="login" placeholder="login" />
                    <input type="password" name="password" placeholder="password" />
                    <input type="submit" value="Login" />

                </form>
            </div>
        )
    }
}
export default LoginForm;