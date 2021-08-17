import {
    Message
  } from 'element-ui'

export function successMessage(message){
    Message({
        message: message,
        showClose: true,
        type: "success",
        duration: 1200,
    });

}


export function errorMessage(message){
    Message({
        message: message,
        showClose: true,
        type: "error",
        duration: 2000,
    });

}