var user: UserProp;

// define the child properties and their types. 

type UserProp = {
    id?: string;
    email?: string;
    lastLogin?: string;
    [key: string]: any;
    setShow: CallableFunction;
}
export declare global {
    declare module globalThis {
       var user: UserProp;
    }
 }

// // Freeze so these can only be defined in this file.
// Object.freeze(globalThis.app);
