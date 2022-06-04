/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
    content: [
        /**
         * HTML. Paths to Django template files that will contain Tailwind CSS classes.
         */

        /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
        '../templates/**/*.html',

        /* 
         * Main templates directory of the project (BASE_DIR/templates).
         * Adjust the following line to match your project structure.
         */
        '../../templates/**/*.html',

        /* 
         * Templates in other django apps (BASE_DIR/<any_app_name>/templates).
         * Adjust the following line to match your project structure.
         */
        '../../**/templates/**/*.html',

        /**
         * JS: If you use Tailwind CSS in JavaScript, uncomment the following lines and make sure
         * patterns match your project structure.
         */
        /* JS 1: Ignore any JavaScript in node_modules folder. */
        // '!../../**/node_modules',
        /* JS 2: Process all JavaScript files in the project. */
        // '../../**/*.js',

        /**
         * Python: If you use Tailwind CSS classes in Python, uncomment the following line
         * and make sure the pattern below matches your project structure.
         */
        '../../**/*.py'
    ],
    important: true,
    theme: {
        extend: {
            colors: {
                'primary': { DEFAULT: '#4B0082', '50': '#AC3BFF', '100': '#A326FF', '200': '#9200FC', '300': '#7A00D4', '400': '#6300AB', '500': '#4B0082', '600': '#2B004A', '700': '#0A0012', '800': '#000000', '900': '#000000' },
                'secondary': {  DEFAULT: '#E3C171',  '50': '#FFFFFF',  '100': '#FEFDF9',  '200': '#F7EED7',  '300': '#F0DFB5',  '400': '#EAD093',  '500': '#E3C171',  '600': '#DAAD42',  '700': '#BE9126',  '800': '#8F6D1C',  '900': '#614913'},

            },
            fontFamily: {
                'patrick-hand' : ['Patrick Hand', 'cursive'],
                'Poppins': ['Poppins', 'sans-serif'],
              },
        },
        container: {
            center: true,
            padding: {
                DEFAULT: '1rem',
                sm: '2rem',
                lg: '4rem',
                xl: '5rem',
                '2xl': '6rem',
              },
        },
    },
    plugins: [
        /**
         * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
         * for forms. If you don't like it or have own styling for forms,
         * comment the line below to disable '@tailwindcss/forms'.
         */
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/line-clamp'),
        require('@tailwindcss/aspect-ratio'),
    ],
}
