# Permissions and Groups Setup

This application uses Django's permissions and groups to control access to user data.

## Groups

- **Editors**: Can view and edit user data.
- **Viewers**: Can only view user data.
- **Admins**: Can view, create, edit, and delete user data.

## Permissions

Custom permissions are defined in the `CustomUser` model:

- `can_view`: Allows viewing of user data.
- `can_create`: Allows creation of new user instances.
- `can_edit`: Allows editing of existing user data.
- `can_delete`: Allows deletion of user instances.

## Views

The following views are protected by these permissions:

- `user_list`: Requires `can_view` permission.
- `edit_user`: Requires `can_edit` permission.
