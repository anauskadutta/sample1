# Build
FROM mcr.microsoft.com/dotnet/sdk:7.0 AS build
WORKDIR /app
COPY . .
RUN dotnet run
RUN dotnet build --no-restore
# RUN dotnet publish -c Release -o ou

# # Run
# FROM mcr.microsoft.com/dotnet/aspnet:7.0
# WORKDIR /app
# COPY --from=build /app/out .
# ENV ASPNETCORE_URLS=http://*:80
# CMD dotnet sample1.dll
