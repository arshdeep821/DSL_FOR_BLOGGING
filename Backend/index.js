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
    // blog_arrays.set(tokens[1], []);
    blog_arrays = [];
}

// 'function function_name = create blog with (key1=value1, key2=value2)\n' -> ["function", "function_name", "key1=value1", "key2=value2"]
const do_function = (tokens) => {
    const functionName = tokens[1];
    // TODO: need to pass in key and value params, but not sure how to handle that
    const params = tokens.slice(2);
    user_functions[functionName] = params;
} 

// ["add", "yeet", "displayed_blog_posts"]
const do_add = (tokens) => {
    const title = tokens[1];
    const blogContent = tokens[2];
    const newBlogDiv = createBlogDiv(title, blogContent);
    // blog_arrays[title].push([title, newBlogDiv]);
    blog_arrays.push([title, newBlogDiv]);
}

const createBlogDiv = (title, blogContent, params) => {
    // TODO: parse params array, and modify div based on that
    // 1. Parse params array (it's of form ["key1=value1", "key2=value2"]), separate by '=' char
    // 2. Iterate over parsed params
    // 3. Switch based on key type (e.g color or category, then make changes to div based on value) 
    for (let param of params) {
        let values = param.split("=");
        let key = value[0];
        let value = value[1];

        switch (key) {
            case "category":
                // TODO: modify category of div
                break;
            case "color":
                // TODO: C
                // https://www.color-hex.com/
                // TODO: modify color of div
                break;
            default:
                break;
        }
    }
    

    const newBlogDiv = document.createElement("div");
    newBlogDiv.id = `blogID-${title}`;
    const newBlogContent = document.createTextNode(blogContent);
    newBlogDiv.appendChild(blogContent);
    return newBlogDiv;
}

// ["remove", "yeet", "displayed_blog_posts"]
const do_remove = (tokens) => {
    // const curr_array = blog_arrays[tokens[2]];

    // for (let item of curr_array) {
    //     if (item[0] === tokens[1]) {
    //         const index = curr_array.indexOf(item);
    //         curr_array.splice(index, 1);
    //         break;
    //     }
    // }

    for (let i = 0; i < blog_arrays.length; i++) {
        if (blog_arrays[i][0] === tokens[1]) {
            blog_arrays.splice(i, 1);
            break;
        }
    }
    // { "displayed_blog_posts: [["yeet1", blog], ["yeet2", blog]]}
}

// ["var", "var_name", "create_day_blog", "Here is some valid text for a blog"],
const do_var = (tokens) => {
    var_name = tokens[1];
    function_name = tokens[2];
    blog_text = tokens[3];
    const params = user_functions[function_name];
    const blog = createBlogDiv(var_name, blog_text, params);
    return blog;
}

// ["if", "night", "then", "if", "midnight", "then", "var", "var_name", "create_day_blog", "Here is some valid text for a blog"]
const do_if = (tokens) => {
    // TODO
    const condition = tokens[1];
    const hours = new Date().getHours();
    const isDay = hours < 18 || hours > 5;
    switch (condition) {
        case "night":
            if(isNight) {
                eval([tokens.slice(3)]);
            }
            break;
        case "day":
            if(isDay) {
                eval([tokens.slice(3)]);
            }
            break;
        default:
            console.log("State error!")
            break;
    }
}

const do_error = () => {
    
}

const do_render = () => {
    const rootElement = document.getElementById("root");
}

module.exports = eval;