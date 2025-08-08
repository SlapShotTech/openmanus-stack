const nextJest = require('next/jest');
const createJestConfig = nextJest({ dir: './' });

module.exports = createJestConfig({
  testEnvironment: 'jsdom',
  // If using ts-jest, enable the following to use the test-specific tsconfig:
  // globals: { 'ts-jest': { tsconfig: 'tsconfig.test.json' } },
});
