import { useEffect, useState } from "react";
import { Card, Image } from "react-bootstrap";
import { NavLink } from "react-router-dom";
import { off, on, trigger } from "../modules/Events";



type UserProp = {
    id?: string;
    email?: string;
    lastLogin?: string;
    [key: string]: any;
    setShow: CallableFunction;
}



const UserCard = (props: UserProp) => {


    const logout = () => {
        fetch('/api/user/logout').then(res =>
            trigger('changeLogin', {})
            
        );


    }

    return (
        <Card bg='dark' border="none" className="p0" style={{border:'none'}}>
            <Card.Body className="d-flex" style={{padding:0}}>
                <Card.Img variant="left" className="rounded-circle" src="https://picsum.photos/50/50" height={50}/>
                    <div style={{paddingLeft:'10px'}}>
                        <h3 style={{padding:0, margin:0}}>
                            {props.user?.id ? props.user?.id : 'Guest'}
                        </h3>
                        {props.user?.id && <a href="#" onClick={logout}>Logout</a>}
                        {!props.user?.id && <NavLink onClick={()=>(props.setShow(false))} to="/login">Login</NavLink>}
                    </div>
            </Card.Body>
        </Card>
    )

}



const User = (props: {setShow : CallableFunction}) => {
    const [user, setUser] = useState<UserProp | null>({setShow: props.setShow}); 
    const [checkLogin, setCheckLogin] = useState<number>(0);
    const [loading, setLoading] = useState<boolean>(true);

    useEffect(() => {
        on('changeLogin', (data: any) => {
            setCheckLogin(checkLogin + 1);
        });

        fetch('/api/me').then(
            (response) => {
                if (response.ok) {
                    response.json().then(
                        (data) => {
                            setUser(data);
                            setLoading(false);
                        }
                    );
                } else {
                    setUser({setShow: props.setShow});

                    setLoading(false);
                }
            }
        );

        
      

        return () => {
            off('login', (data: UserProp) => {
                setCheckLogin(checkLogin + 1);
            });
        };
    }, [checkLogin]);


    useEffect(() => {
        if(user?.id){
            window.user = user;
        }
    }, [user]);


    return (
        
        
        
        <UserCard user={user} setShow={props.setShow}/>

    )
}

export default User;
        