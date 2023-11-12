from setuptools import setup, find_packages

setup(
    name='threadedreturn',
    description="Use threads with return values",
    long_description_content_type='text/markdown',
    long_description=r"""
    # threadedreturn

    `threadedreturn` is a Python package that provides a simple extension to the built-in `Thread` class in the `threading` module. The `ThreadWithReturnValue` class in this package allows you to create threads with return values.

    ## Installation

    You can install `threadedreturn` using `pip`:

    ```bash
    pip install threadedreturn
    ```

    ## Usage

    ### ThreadWithReturnValue

    `ThreadWithReturnValue` is a subclass of `Thread` that enables you to retrieve the return value of a function or method running in a separate thread.

    #### Example

    ```python
    from threadedreturn import ThreadWithReturnValue

    # Define a function to be executed in a separate thread
    def my_function(arg1, arg2):
        # Some time-consuming task
        result = arg1 + arg2
        return result

    # Create a ThreadWithReturnValue instance
    thread = ThreadWithReturnValue(target=my_function, args=(3, 5))

    # Start the thread
    thread.start()

    # Wait for the thread to finish and retrieve the return value
    result = thread.join()

    print("Result:", result)
    ```

    ## Contributing

    If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request on the [GitHub repository](https://github.com/DWAA1660/threadedreturn).

    """,
    version='0.1.2',
    
    packages=find_packages(),
    install_requires=[
    ],
)
