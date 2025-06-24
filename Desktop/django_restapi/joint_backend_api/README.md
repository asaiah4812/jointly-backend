# Django REST API - Vercel Deployment

This Django project is configured for deployment on Vercel with proper static file handling.

## Environment Variables

Set these environment variables in your Vercel dashboard:

- `DATABASE_URL`: Your PostgreSQL database connection string
- `SECRET_KEY`: Django secret key (generate a new one for production)
- `DEBUG`: Set to `False` for production

## Static Files Configuration

The project uses WhiteNoise to serve static files on Vercel. The configuration includes:

1. **WhiteNoise Middleware**: Added to serve static files efficiently
2. **Static Files Storage**: Configured for compression and caching
3. **Build Script**: Automatically collects static files during deployment

## Deployment Steps

1. Push your code to GitHub
2. Connect your repository to Vercel
3. Set the environment variables in Vercel dashboard
4. Deploy

## Troubleshooting

### Admin CSS Not Loading

If Django admin CSS is not loading:

1. Ensure `whitenoise` is in your `requirements.txt`
2. Check that the build script runs successfully
3. Verify static files are collected in the `staticfiles` directory
4. Check Vercel logs for any build errors

### Static Files Issues

- The project uses WhiteNoise for static file serving
- Static files are collected during build process
- Admin static files are served from `/static/admin/` path

## Local Development

For local development, you can run:

```bash
python manage.py runserver
```

Static files will be served by Django's development server. 