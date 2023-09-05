
export interface User {
    email: string,
    firstname: string,
    lastname: string,
}
export interface LoginResponse {
    accessToken : string,
    user : User,
}

export interface LoginRequest {
    email : string,
    password : string
}