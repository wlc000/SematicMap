// @noImplicitAny: false
export {

}

function pick() {
    interface Todo {
        title: string
        description: string
        completed: boolean
    }

    // Pick
    type MyPick<T, K extends keyof T> = { [U in K]: T[U] }
    type TodoPreview = MyPick<Todo, 'title' | 'completed'>
    const todo_1: TodoPreview = {
        title: 'Clean room',
        completed: false,
    }
    // Readonly
    type MyReadonly<T> = { readonly [K in keyof T]: T[K] }
    const todo_2: MyReadonly<Todo> = {
        title: 'Clean room',
        description: 'foobar',
        completed: true
    }
    // TupleToObject
    const tuple = ['tesla', 'model 3', 'model X', 'model Y'] as const
    type TupleToObject<T extends readonly (string | number | symbol)[]> = {
        [K in T[number]]: K
    };
    type result_3 = TupleToObject<typeof tuple>
    const todo_3: result_3 = {
        tesla: 'tesla',
        'model 3': 'model 3',
        'model X': 'model X',
        'model Y': 'model Y'
    }
    // expected {
    // tesla: 'tesla',
    // 'model 3': 'model 3',
    // 'model X': 'model X',
    // 'model Y': 'model Y'
    // }

}
