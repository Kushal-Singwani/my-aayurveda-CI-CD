# Use PHP + Apache as base image
FROM php:8.1-apache

# Enable Apache mod_rewrite (useful for Laravel-style URLs)
RUN a2enmod rewrite

# Copy website files to Apache root directory
COPY . /var/www/html/

# Set working directory
WORKDIR /var/www/html

# Expose port 80 for Apache
EXPOSE 80

# Start Apache in the foreground
CMD ["apache2-foreground"]
