// ["list", "displayed_blog_posts"] -> declaring list
// ["add", "yeet", "displayed_blog_posts"] -> adding to list
// ["remove", "var_name", "displayed_blog_posts"] -> removing from list
// 'var var_name = create_day_blog with text "Here is some valid text for a blog"\n' -> ["var", "var_name", "create_day_blog", "Here is some valid text for a blog"]
// 'function function_name = create blog with (key1=value1, key2=value2)\n' -> ["function", "function_name", "key1=value1", "key2=value2"]
// "if night then add yeet to displayed_blog_posts\n" -> ["if", "night", "then", "add", "yeet", "displayed_blog_posts"]
// 'if night then if midnight then var var_name = create_day_blog with text "Here is some valid text for a blog"\n' -> ["if", "night", "then", "if", "midnight", "then", "var", "var_name", "create_day_blog", "Here is some valid text for a blog"]
/*
inputArray = [
    ["list", "displayed_blog_posts"],
    ["add", "yeet", "displayed_blog_posts"],
    ["remove", "var_name", "displayed_blog_posts"],
    ["var", "var_name", "create_day_blog", "Here is some valid text for a blog"],
    ["function", "function_name", "key1=value1", "key2=value2"],
    ["if", "night", "then", "add", "yeet", "displayed_blog_posts"],
    ["if", "night", "then", "if", "midnight", "then", "var", "var_name", "create_day_blog", "Here is some valid text for a blog"]
]
 */
const initHTMLDocument = '<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><script src="https://cdn.tailwindcss.com"></script></head><body><div id="root"></div></body></html>'
const jsdom = require("jsdom");
const JSDOM = jsdom.JSDOM;
const dom = new JSDOM(initHTMLDocument);
const window = dom.window;
const document = window.document;

const fs = require('fs');

const eval = (inputArray) => {
    const valid = true;
    for (const tokens of inputArray) {
        switch (tokens[0]) {
            case "list":
                do_list(tokens);
                break;
            case "add":
                do_add(tokens);
                break;
            case "remove":
                do_remove(tokens);
                break;
            case "var":
                do_var(tokens);
                break;
            case "function":
                do_function(tokens);
                break;
            case "if":
                do_if(tokens);
                break;
            default:
                do_error();
                valid = false;
                break;
        }
    }

    if (valid) {
        do_render();
    } else {
        console.log('Something Error occured in the backend');
    }
    
}

// Dictionary that maps a color text to it's hex value
const colors = {
    "white": "#FFFFFF",
    "black": "#000000",
    "red": "#FF0000",
    "green": "#00FF00",
    "blue": "#0000FF",
    "yellow": "#FFFF00",
    "purple": "#800080",
    "cyan": "#00FFFF",
    "magenta": "#FF00FF",
    "orange": "#FFA500"
};

const fonts = {
    "verdana": "verdana",
    "courier": "Courier New",
}

const sizes = {
    "small": "16px",
    "medium": "32px",
    "large": "42px"
}

// Dictionary from user-defined blog list name to list of blogs
let blog_arrays; // might need to instantiate here instead of in do_list

// Dictionary from user-defined variable names to values
// example: { "my_blog": "Hello, this is my blog"}
let variables = {};

// Dictionary from user-defined function names to values
// example: { "create_day_blog": fn }
let user_functions = {};

// ["list", "displayed_blog_posts"] -> declaring list
const do_list = (tokens) => {
    blog_arrays = [];
}

let errors = []

// 'function function_name = create blog with (key1=value1, key2=value2)\n' -> ["function", "function_name", "key1=value1", "key2=value2"]
const do_function = (tokens) => {
    const functionName = tokens[1];
    const params = tokens.slice(2);
    user_functions[functionName] = params;
} 

// ["add", "yeet", "displayed_blog_posts"]
const do_add = (tokens) => {
    try {
        const title = tokens[1];
        const blogContent = tokens[2];
        blog_arrays.push([title, variables[title]]);
    } catch (error) {
        errors.push(`List was not instantiated before adding blog ${tokens[1]} to displayed_blog_posts`);
        // console.log(`List was not instantiated before adding blog ${tokens[1]} to displayed_blog_posts`);
    }
}

// function create_day_blog = create blog with (category=day, color=blue)
const createBlogDiv = (title, blogContent, params) => {
    const newBlogDiv = document.createElement("div");
    newBlogDiv.id = `blogID-${title}`;
    newBlogDiv.style.width = '50vw'
    newBlogDiv.style.borderWidth = '5px';
    newBlogDiv.style.padding = '20px';
    newBlogDiv.style.borderStyle = 'solid';
    newBlogDiv.style.borderColor = 'black';
    newBlogDiv.style.textAlign = 'centre';
    newBlogDiv.style.display = 'flex';
    newBlogDiv.style.justifyContent = 'center';
    newBlogDiv.style.alignItems = 'center'; // Center vertically
    newBlogDiv.style.flexDirection = 'column';

    // const newBlogHeader = document.createElement("h3");
    // newBlogHeader.append(title.replaceAll("_", " "));
    // newBlogDiv.appendChild(newBlogHeader)

    const newBlogHeader = document.createElement("h3");
    newBlogHeader.style.textDecoration = 'underline';
    textTitle = title.replaceAll("_", " ");
    newBlogHeader.append(textTitle.charAt(0).toUpperCase() + textTitle.slice(1));
    newBlogDiv.appendChild(newBlogHeader)

    // const newBlogHeader = document.createElement("h3");
    // const capitalizedTitle = title.replaceAll("_", " ").charAt(0).toUpperCase() + title.slice(1).replaceAll("_", " ");
    // newBlogHeader.append(capitalizedTitle);

    const newBlogContent = document.createTextNode(blogContent);
    newBlogDiv.appendChild(newBlogContent);

    for (let param of params) {
        let values = param.split("=");
        let key = values[0];
        let value = values[1];
        
        switch (key) {
            case "color":
                newBlogDiv.style.color = colors[value];
                break;
            case "font":
                // newBlogDiv.style.font = fonts[value];
                newBlogDiv.style.fontFamily = fonts[value];
                break;
            case "size":
                newBlogDiv.style.fontSize = sizes[value];
                break;
            case "image":
                const newImage = createImageElement(value);
                newImage.style.display = 'block';
                newBlogDiv.appendChild(newImage);
                break;
            default:
                console.log("Error: key " + key + " is undefined");
                break;
        }
    }

    return newBlogDiv;
}

const createImageElement = (url) => {
    const newImage = document.createElement('img');
    newImage.width = 100;
    newImage.height = 100;
    newImage.style.maxWidth = '40vw';
    newImage.style.maxHeight = '40vw';
    newImage.src = url;
    return newImage;
}

// ["remove", "yeet", "displayed_blog_posts"]
const do_remove = (tokens) => {
    try {
        for (let i = 0; i < blog_arrays.length; i++) {
            if (blog_arrays[i][0] === tokens[1]) {
                blog_arrays.splice(i, 1);
                break;
            }
        }
    } catch (error) {
        errors.push(`List was not instantiated before removing from displayed_blog_posts`);
        // console.log(`List was not instantiated before removing from displayed_blog_posts`);
    }
}

// ["var", "var_name", "create_day_blog", "Here is some valid text for a blog"],
const do_var = (tokens) => {
    try {
        var_name = tokens[1];
        function_name = tokens[2];
        blog_text = tokens[3];
        const params = user_functions[function_name];
        const blog = createBlogDiv(var_name, blog_text, params);
        variables[var_name] = blog;
    } catch (error) {
        errors.push(`There was an issue with variable: ${tokens[1]}`);
        // console.log(`There was an issue with variable: ${tokens[1]}`);
    }
}

// ["if", "night", "then", "add", "blog_night", "displayed_blog_posts"],
const do_if = (tokens) => {
    try {
        const condition = tokens[1];
        const hours = new Date().getHours();
        const isDay = hours < 18 && hours > 5;
        switch (condition) {
            case "night":
                if(isDay) {
                    return;
                }
                document.getElementById("root").style.backgroundColor = '#3a3e47';
                break;
            case "day":
                if(!isDay) {
                    return;
                }
                document.getElementById("root").style.backgroundColor = '#c3d4fa';
                break;
            default:
                console.log("Undefined condition!")
                break;
        }
    
        switch (tokens[3]) {
            case "add":
                do_add(tokens.slice(3));
                break;
            case "remove":
                do_remove(tokens.slice(3));
                break;
            default:
                console.log("Undefined function!")
                break;
        }
    } catch (error) {
        errors.push(`Something went wrong with if statement involving the condition: ${tokens[1]}`);
        // console.log(`Something went wrong with if statement involving the condition: ${tokens[1]}`);
    }

}

const do_error = () => {
    errors.push(`Something went wrong on the backend, please check your code`);
    // console.log(`Something went wrong on the backend, please check your code`);
}

// blog_arrays = [[name1, blog1], [name2, blog2]]
// const do_render = () => {
//     const rootElement = document.getElementById("root");
//     rootElement.style.width = '100%';
//     rootElement.style.height = '100%';
//     rootElement.style.display = 'flex';
//     rootElement.style.justifyContent = 'center';
//     rootElement.style.flexDirection = 'column';
//     for (let blog of blog_arrays) {
//         rootElement.appendChild(blog[1]);
//     }
//     const htmlContent = dom.serialize();
//     fs.writeFileSync('output.html', htmlContent);
// }

const do_render = () => {
    
    if (errors.length !== 0) {
        console.log(`Errors are present in the code and can not be rendered:`);
        for (let err of errors) {
            console.log(err);
        }
        return;
    }
    
    const rootElement = document.getElementById("root");
    rootElement.style.minWidth = '100vw';
    rootElement.style.minHeight = '100vh';
    rootElement.style.display = 'flex';
    rootElement.style.justifyContent = 'center';
    rootElement.style.alignItems = 'center'; // Center vertically
    rootElement.style.flexDirection = 'column';
    rootElement.style.backgroundColor = '#c3d4fa';
    const mainBlogTitle = document.createElement("h1");
    mainBlogTitle.append("Welcome to my blog!");
    mainBlogTitle.style.fontSize = '100px';
    rootElement.appendChild(mainBlogTitle)

    for (let blog of blog_arrays) {
        const blogElement = blog[1];
        blogElement.style.margin = '10px'; // Add margin for spacing between blogs
        rootElement.appendChild(blogElement);
    }

    const htmlContent = dom.serialize();
    fs.writeFileSync('output.html', htmlContent);
}

module.exports = eval;
