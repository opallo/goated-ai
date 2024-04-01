// A tool to generate a random number within a specified range
type generate_random_number = (_: {
    // The minimum value for the random number
    min: number,
    // The maximum value for the random number
    max: number,
}) => number;

// A tool to fetch data from an external API
type fetch_data_from_api = (_: {
    // The URL of the API endpoint
    api_url: string,
}) => Promise<any>;

// A tool to filter data based on specified criteria
type filter_data = (_: {
    // The data to be filtered
    data: any[],
    // The filter criteria
    filter_criteria: (item: any) => boolean,
}) => any[];

// A tool to transform data into a specific format
type transform_data = (_: {
    // The data to be transformed
    data: any,
    // The transformation function
    transformation_function: (data: any) => any,
}) => any;

// A tool to send notifications to multiple agents
type send_notifications = (_: {
    // The list of agents to notify
    agents: string[],
    // The message to be sent
    message: string,
}) => any;

// A tool to log messages for debugging and monitoring
type log_message = (_: {
    // The message to be logged
    message: string,
    // The log level (e.g., INFO, ERROR)
    log_level: string,
}) => any;
