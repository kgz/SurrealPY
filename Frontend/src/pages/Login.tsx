import { useNavigate } from "react-router-dom";
import { trigger } from "../modules/Events";


const Login = () => {
    const navigate = useNavigate();

    const submit = (e: any) => {
        e.preventDefault();
        const form = e.target;
        const data = new FormData(form);
        const value = Object.fromEntries(data.entries());
        fetch('/api/user/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(value)
        }).then(
            (response) => {
                if (response.ok) {
                    response.json().then(
                        (data) => {
                            trigger('changeLogin', data);
                            navigate(-1)
                        }
                    );
                } else {
                    response.json().then(
                        (data) => {
                            if(data.error) {
                                alert(data.error);
                            }
                            else console.error(data);
                        }
                    );
                }
            }
        );
    };


    
    return (
        <div>
            <h1>Login</h1>
            <form method="POST" action="" autoComplete="off" onSubmit={submit}>
                <input type="text" name="username" placeholder="Username" defaultValue={"test"}/>
                <input type="password" name="password" placeholder="Password" defaultValue={"mypass"}/>
                <input type="submit" value="Login" />
                {/* <Button type="button" variant="primary" onClick={submit}>Primary</Button> */}
            </form>
        </div>
    );
};


export default Login;